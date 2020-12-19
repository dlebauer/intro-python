# using sonic-pi https://sonic-pi.net/

## variables for timing: half (h) dotted quarter (dq), quarter, eighth
h = 2
dq = 1.5
q = 1
e = 0.5

## change the sound of the notes
use_synth :piano

## set the tempo
with_bpm 120 do
  in_thread do
    danny
  end
  
  loop do
    use_synth :pulse
    play 40, release: 0.2
    sleep 0.5
  end
end

## create a function for a set of music
define :danny do
  play_pattern_timed [:fs4, :g4, :a4, :b4, :a4, :b4, :e5, :d5, :b4, :a4, :g4, :e4],
    [e,     e,   e,   dq,  e,   e,   e,   e,   e,   e,  e, q]
  sleep e
  play_pattern_timed [:g4, :b4, :c5, :d5, :e5, :d5, :b4, :g4, :b4, :a4],
    [e, e, e, dq, e, e, e, e, e, h]
end
