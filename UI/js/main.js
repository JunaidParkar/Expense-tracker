const dom = Dkit.init();
dom.revert();

dom.revert();
const cc = new customCursor(dom.id("cursor").get(), false);
cc.getCursor();
dom.revert();

const expenseForm = dom.id("expenseForm").get();
dom.revert();

const showMessage = (message) => {
  dom.revert();
  let div = dom.create("div").get();
  dom.revert();
  let h3 = dom.create("h3").get();
  dom.revert();
  let p = dom.create("p").get();
  dom.revert();
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

if (expenseForm) {
  let formV = new FormValidator(
    expenseForm,
    true,
    [],
    [
      {
        type: "custom_required",
        func: showMessage,
      },
    ]
  );
  formV.validate(() => {
    console.log("validation completed");
  });
}

const cardClickr = () => {
  dom.revert();
  let cards = Array.from(dom.class("card").get());
  dom.revert();
  console.log(cards);
  if (cards.length > 0) {
    cards.forEach((card) => {
      card.addEventListener("click", (e) => {
        console.log(e.target)
        let year = e.target.dataset.year;
        dom.revert();
        let month = Array.from(dom.from(e.target).tag("h4").get())[0].innerText;
        dom.revert();
        console.log("doing");
        window.location.href = `expense.html?year=${year}&month=${month}`;
      });
    });
  }
};
