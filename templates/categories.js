$(document).ready(() => {
  const categories = [
    {
      name: "Category 1",
      description: "A very cool category.",
    },
    {
      name: "Category 2",
      description:
        "A very cool category. A very cool category. A very cool category.",
    },
    {
      name: "Category 3",
      description:
        "A very cool category. A very cool category. A very cool category. A very cool category. A very cool category. A very cool category. A very cool category. A very cool category. A very cool category. A very cool category. A very cool category. A very cool category. A very cool category.",
    },
    {
      name: "Category 4",
      description:
        "A very cool category. A very cool category. A very cool category. A very cool category. A very cool category. A very cool category.",
    },
    {
      name: "Category 5",
      description:
        "A very cool category. A very cool category. A very cool category. A very cool category. A very cool category. A very cool category.",
    },
    {
      name: "Category 6",
      description: "xDDDD",
    },
  ];

  const grid = $("#categoriesGrid");

  const col = `"col-lg-4 col-md-6 col-sm-12 borderWhite"`;

  categories.map((category) => {
    grid.append(`<div class=${col}">
    <a href="#" class="linkNoDeco">
    <div class="card-body m-3">
        <h3 class="card-title">${category.name}</h3>
      <p class="card-text">${category.description}</p>
    </div>
    </a>
  </div>`);
  });
});
