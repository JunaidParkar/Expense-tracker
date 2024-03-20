const dom = Dkit.init();

window.onload = () => {
  let d = new Date()
  var today = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, '0')}`;
  dom.id("date").get() ? dom.id("date").get().max = today : ""
}

const cc = new customCursor(dom.id("cursor").get(), false);
cc.getCursor();

const showMessage = (message) => {
  let div = dom.create("div").get();
  let h3 = dom.create("h3").get();
  let p = dom.create("p").get();
  div.classList.add("messageAlert");
  h3.textContent = "Form alert";
  p.textContent = message;
  div.appendChild(h3);
  div.appendChild(p);
  document.body.append(div);
  setTimeout(() => {
    document.body.removeChild(div);
  }, 3000);
};

const cancel_conf = () => {
  Array.from(dom.class("confirm_screen").get())[0].style.display = "none"
}