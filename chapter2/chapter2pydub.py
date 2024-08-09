from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('roar.mp3')

# Menyimpan file audio
audio.export('roar.mp3', format='mp3')

clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('roar.mp3', format='mp3')

combined_audio = audio + clipped_audio
combined_audio.export('roar.mp3', format='mp3')

audio.export('roar.wav', format='wav')

louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('roar.mp3', format='mp3')

