# yan_docker_speech_to_text

```bash
docker build -t yan_speech_to_text:1.0.1 .

docker run -it -v /Users/yan/Downloads/:/yan/ yan_speech_to_text:1.0.1
```


```python
from yan_tts import speech_to_text

speech_to_text(input_wav_file = "/yan/test1.wav")
```

<img src="WX20201015-203355%402x.png" height="100">

