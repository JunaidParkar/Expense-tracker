const dom = Dkit.init()

dom.revert()
dom.id("cursor")

const cc = new customCursor(dom.get(), false)
cc.getCursor()
dom.revert()

dom.id("expenses-slider-parent")
const slider_parent = dom.get()
dom.revert()

dom.class("card")
console.log(Array.from(dom.get())[0])