const scroller = new scrollManager();
scroller.addListener();

const head = dom.tag("head").get()[0];

if (dom.from(head).tag("title").get()[0].textContent == "Expense") {
  var params = new URLSearchParams(window.location.search);
  var year = params.get("year");
  var month = params.get("month");
  if (!year || !month) {
    window.location.href = "index.html";
  }
  dom.revert();
  dom.id("heading").get().textContent = month + " " + year;
  let months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  showSpecificMonthData(`${year}-${months.indexOf(month)}`);
}

const getBack = () => (window.location.href = "index.html");

const expenseForm = dom.id("expenseForm").get();

const addTransaction = () => {
  let amount = dom.id("amount").get()
  let type = dom.id("type").get();
  let description = dom.id("description").get()
  let date = dom.id("date").get()
  let category = dom.id("category").get()
  let cnf = confirm(`Are you sure you want to continue with these datas`)
  // eel.addTransaction(amount.value, category.value, description.value, type.value == "Check In" ? "positive" : "negative", date.value)()
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
    addTransaction()
  });
}