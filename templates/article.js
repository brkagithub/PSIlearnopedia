$(document).ready(() => {
  const categories = ["Family", "Lifestyle", "Holiday", "Food"];

  const categoriesEl = $("#categories");
  const authorEl = $("#author");

  categories.map((categoryName) => {
    categoriesEl.append(
      `<button class="rounded-circle categoryChip">${categoryName}</button>`
    );
  });

  authorEl.append(`<h3>profile pic</h3>
    <h3>Jessica Wildfire</h3>`);
});
