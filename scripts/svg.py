def create_svg(contributions):
    return f"""
<svg xmlns="http://www.w3.org/2000/svg"
width="620"
height="148">

<text
x="20"
y="70"
font-size="50">
{contributions}
</text>

</svg>
"""