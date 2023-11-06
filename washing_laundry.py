# Washing Laundry

Tasks
sort laundry
wash laundry
remove laundry
return laundry to basket

Pattern Rec
If delicate, delicate basket
If white, white basket
If blue, blue basket
Else, 4th basket

Abstractions
Ignore bedding and towels

Sequence
for item in dirty_clothes
    if (delicate)
        add to delicate basket
    else-if white
        add to white basket
    else-if red
        add to red basket
    else
        leave in dirty_clothes

# list baskets = [white basket, red basket, delicate basket, dirty_clothes]

# for basket in baskets
    for item in basket
        place in washing machine
    add soap to machine
    if (delicate_basket)
        set delicate settings
    else
        regular settings

    if (washing == done)
    ....remove items