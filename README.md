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

<img src="WX20201015-203355%402x.png" height="100">


<table>
  <thead>
    <tr>
      <th>Input Photo</th>
      <th>Output Tagged Photo</th>
      <th>Output Detected Text</th>
    </tr>
  </thead>
  <tr>
    <td>
      <img src="https://raw.githubusercontent.com/yanliang12/yan_ocr/main/test4.png" height="180">
    </td>
    <td>
      <img src="https://raw.githubusercontent.com/yanliang12/yan_ocr/main/test4_output.png" height="180">
    </td>
    <td>
<pre>
[
  {
    'text': 'LA U R EN', 
    'score': 0.3055954575538635, 
    'coordinate': [[590, 31], 
                  [1021, 31], 
                  [1021, 122], 
                  [590, 122]]
  }, 
  {
    'text': 'RAL PH', 
    'score': 0.24870802462100983, 
    'coordinate': [[177, 35], 
                  [533, 35], 
                  [533, 121], 
                  [177, 121]]
   }
]    
</pre>
</td>
</tr>
</table>
