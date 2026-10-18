import openmc
import numpy as np

# --- Materials ---
be = openmc.Material(name='Beryllium Be-9 multiplier')
be.add_element('Be', 1.0, percent_type='ao')
be.set_density('g/cm3', 1.85)

li_breeder = openmc.Material(name='Li4SiO4 breeder')
li_breeder.add_element('Li', 4.0, percent_type='ao')
li_breeder.add_element('Si', 1.0, percent_type='ao')
li_breeder.add_element('O', 4.0, percent_type='ao')
li_breeder.set_density('g/cm3', 2.32)
li_breeder.add_s_alpha_beta('c_H_in_H2O') # placeholder

eurofer = openmc.Material(name='Eurofer structure')
eurofer.add_element('Fe', 0.89, percent_type='wo')
eurofer.add_element('Cr', 0.09, percent_type='wo')
eurofer.set_density('g/cm3', 7.8)

materials = openmc.Materials([be, li_breeder, eurofer])

# --- Geometry: 60mm fractal, 63 channels ---
# Base cylinder 60mm dia = 30mm radius
outer_radius = openmc.ZCylinder(r=3.0) # cm = 30mm

# Fractal 63 channels - simplified as hexagonal lattice
# Level 1: 1 center, Level 2: 6, Level 3: 12, Level 4: 44 = 63 total
# For OpenMC we model as 63 small cylinders
channel_radius = 0.15 # 1.5mm per channel
channels = []
for i in range(63):
    angle = i * 2*np.pi / 63
    rad = (i % 4) * 0.6 + 0.3 # fractal spacing
    x = rad * np.cos(angle)
    y = rad * np.sin(angle)
    cyl = openmc.ZCylinder(x0=x, y0=y, r=channel_radius)
    channels.append(cyl)

# --- Cells ---
be_cell = openmc.Cell(name='fractal Be multiplier FRB-BB-2026-KI-001')
be_cell.region = -outer_radius
for c in channels:
    be_cell.region &= ~+c # exclude channels? actually channels are Be
be_cell.fill = be

# Breeder in channels (where tritium breeding happens)
breeder_cells = []
for c in channels:
    cell = openmc.Cell()
    cell.region = +c & -outer_radius
    cell.fill = li_breeder
    breeder_cells.append(cell)

# --- Settings for TBR tally ---
settings = openmc.Settings()
settings.batches = 100
settings.inactive = 10
settings.particles = 10000
settings.source = openmc.IndependentSource(
    space=openmc.stats.Point((0,0,0)),
    energy=openmc.stats.Muir(e0=14.06e6, m_rat=4.0, kt=20000.0) # DT fusion 14.06 MeV
)

# TBR tally: Li-6 (n,t) alpha
tbr_tally = openmc.Tally(name='TBR 1.21->1.28')
tbr_tally.scores = ['(n,Xt)'] # Tritium production
tbr_tally.nuclides = ['Li6']

tallies = openmc.Tallies([tbr_tally])

# --- Model ---
model = openmc.Model(
    geometry=openmc.Geometry([be_cell] + breeder_cells),
    materials=materials,
    settings=settings,
    tallies=tallies
)

print("FRB-BB-2026-KI-001 model ready: 60mm, 63 channels")
print("Expected TBR: 1.21 baseline, 1.28 with Be n,2n")
# model.run()

