
TODO: Rename this to something like:

Server one file for multiple url pahts


This one redirects all traffic (including images and favicons) 
to a single `target.html` file at the root of the
S3 bucket. 

The change is made via a native CloudFront Function 
(not a Lambda Edge function) that adjusted the header
uri key at the "Visitor Request" part of the process
which is the first thing that happens in the function
chain. 

TODO: Add an href with a random string for a link
on the page to make it easier to see that all
traffic goes to the same page. 
