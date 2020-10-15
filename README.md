# yan_docker_speech_to_text

```bash
docker build -t yan_speech_to_text:1.0.1 .

docker run -it -v /Users/yan/Downloads/:/yan/ yan_speech_to_text:1.0.1
```


```python
>>> from yan_tts import speech_to_text
>>> 
>>> text = speech_to_text(input_wav_file = "test3.wav")
sox WARN rate: rate clipped 116 samples; decrease volume?
sox WARN dither: dither clipped 100 samples; decrease volume?
>>> 
>>> print(text)
timewell in the way for races to mason the moon in nineteen ninety two by solar sale
three small is to commemorate columbus's journal the new world five hundred years ago and the ones at the moon it's a promote the use of solar sailin space exploration
>>> 
```

<table>
  <thead>
    <tr>
      <th>Input Speech</th>
      <th>Output Text</th>
    </tr>
  </thead>
  <tr>
    <td>
      <img src="WX20201015-203355%402x.png" height="100">
    </td>
    <td>
<pre>
timewell in the way for races to mason the 
moon in nineteen ninety two by solar sale
three small is to commemorate columbus's 
journal the new world five hundred years 
ago and the ones at the moon it's a promote 
the use of solar sailin space exploration
</pre>
</td>
</tr>
</table>
