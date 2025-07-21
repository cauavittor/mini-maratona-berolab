from dino_runner.components.game import Game

if __name__ == "__main__":
    game = Game()
    
    sound_paths = {
        'jump': 'C:\\Users\\CAUA\\Downloads\\sons_jump_sound.wav',
        'death': 'C:\\Users\\CAUA\\Downloads\\sons_death_sound.wav', 
        'score': 'C:\\Users\\CAUA\\Downloads\\sons_score_sound.wav'
    }
    
    game.setup_sounds(sound_paths)
    
    game.setup_background_music('C:\\Users\\CAUA\\Downloads\\backgroundSound.mp3')
    
    game.execute()
