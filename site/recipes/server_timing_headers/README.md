This recipe shows how to turn on
ServerTiming response headers. As of
Sept. 2022, there's not a native way
to do it with CDK functions. The
solution is to edit the object with
the `.add_override()` method.

Setting the `Enabled` value to `True`
preps the headers but they won't turn
on without setting `SamplingRate`
which determines what percentage of
traffic to turn the headers on for.
(The value should be an integer between
`0` and `100` to represent the percentage)
