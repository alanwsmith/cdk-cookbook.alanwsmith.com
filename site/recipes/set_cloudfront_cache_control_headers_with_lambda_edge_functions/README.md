This sets cache control headers


The example sets one from origin
which is what cloudfront should use
in determing when it needs to go back 
to origin and then it also sets one
in the visotor response. That is the
one that's sent back to the browser. 

The idea here is that you can have 
the origin file not change, but the
cloudfront file update data via
it's functions (e.g. adjusting headers)
frequently without having to go 
back to origin. 





