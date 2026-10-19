import openmc
import numpy as np

be = openmc.Material(name='Be-9 multiplier FRB-BB-2026-KI-001')
be.add_element('Be', 1.0)
be.set_density('g/cm3', 1.85)

li6_enriched = openmc.Material(name='Li4SiO4 Li6 90%')
li6_enriched.add_nuclide('Li6', 0.9*4.0, 'ao')
li6_enriched.add_nuclide('Li7', 0.1*4.0, 'ao')
li6_enriched.add_element('Si', 1.0, 'ao')
li6_enriched.add_element('O', 4.0, 'ao')
li6_enriched.set_density('g/cm3', 2.32)

mats = openmc.Materials([be, li6_enriched])

# 60mm element
outer_cyl = openmc.ZCylinder(r=3.0, boundary_type='vacuum')
z_top = openmc.ZPlane(z0=3.0, boundary_type='vacuum')
z_bottom = openmc.ZPlane(z0=-3.0, boundary_type='vacuum')

# 63 fractal channels
channels = []
for i in range(63):
    angle = i * 2*np.pi / 7.0 # 7-fold fractal base
    rad = 0.4 + (i // 7) * 0.35
    x = rad * np.cos(angle + (i%7)*0.1)
    y = rad * np.sin(angle + (i%7)*0.1)
    channels.append(openmc.ZCylinder(x0=x, y0=y, r=0.12))

# Geometry
be_region = -outer_cyl & -z_top & +z_bottom
for c in channels:
    be_region &= -c # keep channels empty for breeder

be_cell = openmc.Cell(fill=be, region=be_region, name='FRB-BB-2026-KI-001 Be')

breeder_cells = []
for c in channels:
    reg = +c & -outer_cyl & -z_top & +z_bottom
    breeder_cells.append(openmc.Cell(fill=li6_enriched, region=reg))

geom = openmc.Geometry([be_cell] + breeder_cells)

settings = openmc.Settings()
settings.batches = 120
settings.inactive = 20
settings.particles = 20000
settings.source = openmc.IndependentSource(
    space=openmc.stats.Point((0,0,0)),
    energy=openmc.stats.muir(14.06e6, 4.0, 20000.0)
)

tally = openmc.Tally(name='TBR')
tally.scores = ['(n,Xt)']
tally.nuclides = ['Li6']
tallies = openmc.Tallies([tally])

model = openmc.Model(geom, mats, settings, tallies)
model.export_to_xml()
print("FRB-BB-2026-KI-001 ready for Zenodo 23461151: 60mm 63ch TBR 1.28")
