const dom = Dkit.init();
const scroller = new scrollManager()

scroller.addListener()

dom.revert();
dom.id("cursor");

const cc = new customCursor(dom.get(), false);
cc.getCursor();
dom.revert();

const expenseForm = dom.id("expenseForm").get()
dom.revert()

const showMessage = (message) => {
    dom.revert()
    let div = dom.create("div").get()
    dom.revert()
    let h3 = dom.create("h3").get()
    dom.revert()
    let p = dom.create("p").get()
    dom.revert()
    div.classList.add("messageAlert")
    h3.textContent = "Form alert"
    p.textContent = message
    div.appendChild(h3)
    div.appendChild(p)
    document.body.append(div)
    setTimeout(() => {
        document.body.removeChild(div)
    }, 3000);
}

let formV = new FormValidator(expenseForm, true, [], [
    {
      type: "custom_required",
      func: showMessage
    }
  ])
formV.validate(() => {
    console.log("validation completed")
})