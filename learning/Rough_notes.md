

Brackets Doubts : 

Round brackets () — "Do this action"

Whenever you see () right after a word, it means "run this thing now." Like print() means "go print it." If there's no (), you're just talking about the thing, not making it do anything.

Square brackets [] — "Open the box and take something out, OR make a new box"

Two uses, easy to tell apart:

If [] is alone, with nothing before it, you are making a new list. Like cart = [item1, item2] — you are packing things into a box called cart.

If [] comes right after a name, like items['price'], you are opening that box and picking out one thing from inside it — here you're picking out the value stored at 'price'.

Think of items as a tiffin box with sections labelled name, price, quantity. Writing items['price'] is like opening the tiffin and taking out only the price section.

Curly brackets {} — "This is a dictionary" or "put the real value here"

When you write {"name": "Anavar", "price": 95.65} you're building that tiffin box itself — labels and food together.

Inside an f-string, like f"{items['name']}", the {} means "don't print these words as-is, actually go get the real value and put it here." So {items['name']} becomes the actual name, not the text items['name'].

Now total += line_total — simple example:

Imagine you keep a small notebook (total) where you write down your total spending. Every time you buy something new (line_total), you don't throw away the old number — you add the new item's cost to what was already written, and write the new total back in the notebook.

So total = total + line_total and total += line_total are the exact same thing. The second one is just a shortcut, saved typing.

One line to remember all of this:

() = do it. [] = open the box and take/put something. {} = this is the box itself, or "put the real answer here" inside an f-string.