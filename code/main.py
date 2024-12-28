from settings import *
from custom_timer import Timer

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Space Shooter")
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

while not window_should_close():
    # Updates
    
    dt = get_frame_time()
    player.update(dt)
    meteor_timer.update()
    for meteor in meteors:
        meteor.update(dt)
        if check_collision_recs(meteor.rect, laser.rect):
            meteors.remove(meteor)
            fire = False
        if check_collision_recs(meteor.rect, player.rect):
            close_window()
        
    if is_key_pressed(KEY_SPACE):
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

close_window()
