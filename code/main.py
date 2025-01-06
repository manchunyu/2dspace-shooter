from settings import *
from custom_timer import Timer

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Space Shooter")
init_audio_device()

music = load_music_stream(join("..", "audio", "music.wav"))
laser_sound = load_sound(join("..", "audio", "laser.wav"))

# font = load_font(join("..", "font", "Stormfaze.otf"))

play_music_stream(music)

# set_target_fps(60)

player = Player()
meteor = Meteor()
laser = Laser()
meteors = []
stars = [Star() for _ in range(20)]
fire = False

def create_meteor():
    meteors.append(Meteor())
    
meteor_timer = Timer(METEOR_TIMER_DURATION, True, True, create_meteor)
explosion_timer = Timer(1, False, False, )
while not window_should_close():
    # Updates
    
    dt = get_frame_time()
    update_music_stream(music)
    player.update(dt)
    meteor_timer.update()
    for meteor in meteors:
        meteor.update(dt)
        if check_collision_recs(meteor.rect, laser.rect):
            meteors.remove(meteor)
            fire = False
        if check_collision_recs(meteor.rect, player.rect):
            unload_audio_stream(music)
            close_audio_device()
            close_window()

        
    if is_key_pressed(KEY_SPACE):
        play_sound(laser_sound)
        fire = True
        laser.update(player.pos)

    if fire:
        laser.fire(dt)
        if laser.pos.y < 0:
            fire = False


    begin_drawing()

    # Background
    clear_background(BG_COLOR)
    for star in stars:
        draw_texture_v(star.texture, star.pos, WHITE)
    draw_fps(0, 0)
    
    # Draw moving sprites
    for meteor in meteors:
        draw_texture_v(meteor.texture, meteor.pos, WHITE)

    draw_texture_v(player.texture, player.pos, WHITE)
    
    if fire:
        draw_texture_v(laser.texture, laser.pos, WHITE)
    draw_text(str(int(get_time())), (WINDOW_WIDTH - FONT_SIZE) // 2, 100, FONT_SIZE, WHITE)

    end_drawing()
    # print(len(meteors))
unload_audio_stream(music)
close_audio_device()
close_window()
