import pydisort

ds = pydisort.disort()
flags = {'usrtau': True, 'plank': True,}
ds.set_
ds.set_flags(flags)
ds.set_atmosphere_dimension(nlyr = 1, nstr = 16, nmom = 16)
ds.set_intensity_dimension(nuphi = 1, nutau = 2, numu = 6)
ds.seal()
# pmom = pydisort.get_phase_function(nmom = 16, model = "isotropic")
# ds.set_optical_thickness([0.1])
# ds.set_single_scattering_albedo([1.0])
# ds.set_phase_moments(pmom)
ds.set_user_optical_depth([0.0, 0.1])
# ds.set_user_cosine_polar_angle([-1.0, -0.5, -0.1, 0.1, 0.5, 1.0])
# ds.set_user_azimuthal_angle([0.0])
# ds.umu0 = 1.0
# ds.fbeam = 3.14159
rad, flx = ds.run()