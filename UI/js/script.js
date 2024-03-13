const scroller = new scrollManager();
scroller.addListener();

dom.revert();
const head = dom.tag("head").get()[0];
dom.revert();
if (dom.from(head).tag("title").get()[0].textContent == "Expense") {
  var params = new URLSearchParams(window.location.search);
  var year = params.get("year");
  var month = params.get("month");
  if (!year || !month) {
    window.location.href = "index.html"
  }
  dom.revert()
  dom.id("heading").get().textContent = month + " " + year
  let months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  showSpecificMonthData(`${year}-${months.indexOf(month)}`)
}

dom.revert();


const getBack = () => window.location.href = "index.html"