# -*- coding: utf-8 -*-
import requests
WELCOME_MSG = "Benvenuto su A. C. San Michele, puoi chiedermi di riprodurre l'ultimo podcast."
WELCOME_REPROMPT_MSG = "Puoi dire, riproduci il podcast, per iniziare."
WELCOME_PLAYBACK_MSG = "Stavi ascoltando {}. Desideri riprendere?"
WELCOME_PLAYBACK_REPROMPT_MSG = "Puoi dire Si per riprendere oppure No per ascoltare dall'inizio"
DEVICE_NOT_SUPPORTED = "Mi dispiace, la skill non è supportata da questo device"
LOOP_ON_MSG = "Funzionalità ripeti abilitata."
LOOP_OFF_MSG = "Funzionalità ripeti disabilitata."
HELP_MSG = WELCOME_MSG
HELP_PLAYBACK_MSG = WELCOME_PLAYBACK_MSG
HELP_DURING_PLAY_MSG = "Stai ascoltando A. C. San Michele. Puoi dire, Avanti o Indietro per navigare nella playlist. In ogni momento, puoi dire Pause per mettere in pause l'ascolto e Riprendi per riprendere."
STOP_MSG = "A presto."
EXCEPTION_MSG = "Mi dispiace, questo comando non è valido. Se hai bisogno, dici Aiuto per vedere cosa puoi chiedermi."
PLAYBACK_PLAY = "Stai ascoltando {}"
PLAYBACK_PLAY_CARD = "In riproduzione: {}"
PLAYBACK_NEXT_END = "Hai raggiunto la fine della playlist"
PLAYBACK_PREVIOUS_END = "Hai raggiunto l'inizio della playlist"

DYNAMODB_TABLE_NAME = "Audio-Player-ACSanMichele"

AUDIO_DATA = requests.get('https://dariocast.altervista.org/quisutdeus/lista_alexa.php').json()
# AUDIO_DATA = [
#     {
#         "title": "Episode 22",
#         "url": "https://feeds.soundcloud.com/stream/459953355-user-652822799-episode-022-getting-started-with-alexa-for-business.mp3",
#     },
#     {
#         "title": "Episode 23",
#         "url": "https://feeds.soundcloud.com/stream/476469807-user-652822799-episode-023-voicefirst-in-2018-where-are-we-now.mp3",
#     },
#     {
#         "title": "Episode 24",
#         "url": "https://feeds.soundcloud.com/stream/496340574-user-652822799-episode-024-the-voice-generation-will-include-all-generations.mp3",
#     }
# ]