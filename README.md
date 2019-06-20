# LilyMath
A Python program that generates random musical notation (letters a-f) in a list for a selected period of time. That content is then converted to a Lilypond file and played as music.

The key to the project is using math to create musical expression. 

This was very much an experimental process to see what each of the programs could handle. As it turns out Lilypond isn't really designed to handle the kind of heavy data that Python was putting out. That being said, I eventually found workarounds.

For instance, once put into a list and copied to a clipboard the Python ouptut could be cleaned up using the find and replace option in Word. After that it was a matter of loading the data into Lilypond which became a much more difficult ordeal.

I tried numerous time increments starting first at three minutes then cutting it shorter and shorter. I assumed five seconds would be long enough but it turns out one second is the magic number. One second produces three pages of sheet music in Lilypond. The results are listed as pages 1-3 in the repo.

