import RT_utility as rtu
import RT_camera as rtc
import RT_renderer as rtren
import RT_material as rtm
import RT_scene as rts
import RT_object as rto
import RT_integrator as rti
import RT_light as rtl
import RT_texture as rtt

def renderMirrors():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 20
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_ground = rtm.Lambertian(rtu.Color(0.8, 0.8, 0.0))
    mat_center = rtm.Lambertian(rtu.Color(0.7, 0.3, 0.3))
    mat_ball = rtm.Lambertian(rtu.Color(0.1, 0.3, 0.5))

    tex_checker_bw = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))
    tex_checker = rtt.CheckerTexture(0.12, rtu.Color(.2, .3, .1), rtu.Color(.9, .9, .9))
    tex_solid = rtt.SolidColor(rtu.Color(0.8, 0.2, 0.5))

    mat_tex_checker_bw = rtm.TextureColor(tex_checker_bw)
    mat_tex_checker = rtm.TextureColor(tex_checker)
    mat_tex_solid = rtm.TextureColor(tex_solid)

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_center))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_tex_checker))
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_tex_solid))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week07_texture_sky.png')    

def renderEarth():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 20
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_ground = rtm.Lambertian(rtu.Color(0.8, 0.8, 0.0))
    mat_center = rtm.Lambertian(rtu.Color(0.7, 0.3, 0.3))
    mat_ball = rtm.Lambertian(rtu.Color(0.1, 0.3, 0.5))

    tex_checker_bw = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))
    tex_checker = rtt.CheckerTexture(0.12, rtu.Color(.2, .3, .1), rtu.Color(.9, .9, .9))
    tex_solid = rtt.SolidColor(rtu.Color(0.8, 0.2, 0.5))
    tex_earth = rtt.ImageTexture("./textures/earthmap.png")
    tex_basketball = rtt.ImageTexture("./textures/basketball.jpg")
    tex_soccer = rtt.ImageTexture("./textures/soccer.jpg")
    tex_pepsi = rtt.ImageTexture("./textures/pepsi.jpg")

    mat_tex_checker_bw = rtm.TextureColor(tex_checker_bw)
    mat_tex_checker = rtm.TextureColor(tex_checker)
    mat_tex_solid = rtm.TextureColor(tex_solid)
    mat_tex_earth = rtm.TextureColor(tex_earth)
    mat_tex_basketball = rtm.TextureColor(tex_basketball)
    mat_tex_soccer = rtm.TextureColor(tex_soccer)
    mat_tex_pepsi = rtm.TextureColor(tex_pepsi)

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_earth))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_tex_pepsi))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_tex_basketball))
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_tex_soccer))

    world.add_object(rto.Quad(rtu.Vec3(1.0, 0.0, -1), rtu.Vec3(1.0, 2.0, -1), rtu.Vec3(1.0, 0.0, 1), mat_tex_pepsi))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week07_texture_earth_sky3.png')    


if __name__ == "__main__":
    # renderMirrors()
    renderEarth()


