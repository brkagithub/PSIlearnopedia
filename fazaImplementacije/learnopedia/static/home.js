$(document).ready(() => {
  const articles = [
    {
      title: "Impact of family",
      author: {
        username: "brka",
      },
      likes: 89,
      content:
        "Lorem ipsum dolor sit amet. Ea cumque magni ab delectus sunt et magni excepturi cum magni mollitia nam natus consectetur qui animi magnam sit deserunt omnis. Eum repellat nulla aut omnis perspiciatis et quia repellat qui accusamus harum in enim velit ut tenetur atque. Ea officiis repudiandae qui nulla error aut quibusdam omnis non doloribus quasi est dicta esse et obcaecati explicabo. Est galisum iusto ut eveniet maiores nam fugit eaque et soluta saepe et natus saepe sit numquam dolore est libero cumque.",
      categories: ["Family", "Lifestyle", "Holiday"],
      shortDescription:
        "Family is very important. Family is very important. Family is very important. Family is very important.",
      previewImgURL:
        "https://grillshop.rs/wp-content/uploads/2021/05/190524-classic-american-cheeseburger-ew-207p-2870431.jpg",
    },
    {
      title: "Impact of pokemons",
      author: {
        username: "ilijakiller8592502",
      },
      likes: 39,
      content:
        "Lorem ipsum dolor sit amet. Ea cumque magni ab delectus sunt et magni excepturi cum magni mollitia nam natus consectetur qui animi magnam sit deserunt omnis. Eum repellat nulla aut omnis perspiciatis et quia repellat qui accusamus harum in enim velit ut tenetur atque. Ea officiis repudiandae qui nulla error aut quibusdam omnis non doloribus quasi est dicta esse et obcaecati explicabo. Est galisum iusto ut eveniet maiores nam fugit eaque et soluta saepe et natus saepe sit numquam dolore est libero cumque.",
      categories: ["Pokemon", "Games"],
      shortDescription: "Have you ever wondered what was your first Pokemon?",
      previewImgURL:
        "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8YnVyZ2VyfGVufDB8fDB8fA%3D%3D&w=1000&q=80",
    },
    {
      title: "Impact of family",
      author: {
        username: "brka",
      },
      likes: 89,
      content:
        "Lorem ipsum dolor sit amet. Ea cumque magni ab delectus sunt et magni excepturi cum magni mollitia nam natus consectetur qui animi magnam sit deserunt omnis. Eum repellat nulla aut omnis perspiciatis et quia repellat qui accusamus harum in enim velit ut tenetur atque. Ea officiis repudiandae qui nulla error aut quibusdam omnis non doloribus quasi est dicta esse et obcaecati explicabo. Est galisum iusto ut eveniet maiores nam fugit eaque et soluta saepe et natus saepe sit numquam dolore est libero cumque.",
      categories: ["Family", "Lifestyle", "Holiday"],
      shortDescription:
        "Family is very important. Family is very important. Family is very important. Family is very important.",
      previewImgURL:
        "https://grillshop.rs/wp-content/uploads/2021/05/190524-classic-american-cheeseburger-ew-207p-2870431.jpg",
    },
    {
      title: "Impact of pokemons",
      author: {
        username: "ilijakiller8592502",
      },
      likes: 39,
      content:
        "Lorem ipsum dolor sit amet. Ea cumque magni ab delectus sunt et magni excepturi cum magni mollitia nam natus consectetur qui animi magnam sit deserunt omnis. Eum repellat nulla aut omnis perspiciatis et quia repellat qui accusamus harum in enim velit ut tenetur atque. Ea officiis repudiandae qui nulla error aut quibusdam omnis non doloribus quasi est dicta esse et obcaecati explicabo. Est galisum iusto ut eveniet maiores nam fugit eaque et soluta saepe et natus saepe sit numquam dolore est libero cumque.",
      categories: ["Pokemon", "Games"],
      shortDescription: "Have you ever wondered what was your first Pokemon?",
      previewImgURL:
        "https://grillshop.rs/wp-content/uploads/2021/05/190524-classic-american-cheeseburger-ew-207p-2870431.jpg",
    },
    {
      title: "Impact of family",
      author: {
        username: "brka",
      },
      likes: 89,
      content:
        "Lorem ipsum dolor sit amet. Ea cumque magni ab delectus sunt et magni excepturi cum magni mollitia nam natus consectetur qui animi magnam sit deserunt omnis. Eum repellat nulla aut omnis perspiciatis et quia repellat qui accusamus harum in enim velit ut tenetur atque. Ea officiis repudiandae qui nulla error aut quibusdam omnis non doloribus quasi est dicta esse et obcaecati explicabo. Est galisum iusto ut eveniet maiores nam fugit eaque et soluta saepe et natus saepe sit numquam dolore est libero cumque.",
      categories: ["Family", "Lifestyle", "Holiday"],
      shortDescription:
        "Family is very important. Family is very important. Family is very important. Family is very important.",
      previewImgURL:
        "https://media.istockphoto.com/photos/juicy-hamburger-on-white-background-picture-id1206323282?k=20&m=1206323282&s=612x612&w=0&h=yatlq6BHRCCvoTzFZLSwaJc0O8Quct_tRPWtH0dj9Fc=",
    },
    {
      title: "Impact of pokemons",
      author: {
        username: "ilijakiller8592502",
      },
      likes: 39,
      content:
        "Lorem ipsum dolor sit amet. Ea cumque magni ab delectus sunt et magni excepturi cum magni mollitia nam natus consectetur qui animi magnam sit deserunt omnis. Eum repellat nulla aut omnis perspiciatis et quia repellat qui accusamus harum in enim velit ut tenetur atque. Ea officiis repudiandae qui nulla error aut quibusdam omnis non doloribus quasi est dicta esse et obcaecati explicabo. Est galisum iusto ut eveniet maiores nam fugit eaque et soluta saepe et natus saepe sit numquam dolore est libero cumque.",
      categories: ["Pokemon", "Games"],
      shortDescription: "Have you ever wondered what was your first Pokemon?",
      previewImgURL:
        "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F9%2F2021%2F07%2F13%2FUltimate-Veggie-Burgers-FT-Recipe-0821.jpg&q=60",
    },
  ];

  const grid = $("#articleGrid");

  const col = `"col-lg-4 col-md-6 col-sm-12"`;

  articles.map((article) => {
    grid.append(`<div class=${col}>
    <a href="../../templates/article.html" class="linkNoDeco">
      <div class="card m-3" >
      <img src="${article.previewImgURL}" class="card-img-top" alt="...">
      <div class="card-body">
      <div class="flex">
      <h4 class="card-title">${article.title}</h5>
      <p class="card-text card-likes">${article.likes} likes</p>
      </div>
      <p class="card-text card-author">By ${article.author.username}</p>
      </div>

      <div class="card-body">
      <p class="card-text card-desc">${article.shortDescription}</p>
      </div>
      </div>
    </a>
    </div>`);
  });
});
