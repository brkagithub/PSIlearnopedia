$(document).ready(() => {
  const profile = {
    fullName: "Jessica Wildfire",
    username: "Jess_W",
    description:
      "Hi im Jessica. I'm a human right activist and a cat mom. I am an alumni of Harvard University of Law.If you'd like to collaborate feel free to find me at jessicalovescats@gmail.com",
    popularArticles: [
      {
        title: "International day of happiness",
        description:
          "There's more behind the International Day of Happiness than you might think. Find out more by reading the article and answering the questions.",
        likes: 89,
        dislike: 2,
        slug: "article",
        daysAgo: 1,
      },
      {
        title: "Human rights",
        description:
          "Whereas recognition of the inherent dignity and of the equal and inalienable rights of all members of the human family is the foundation of freedom, justice and peace in the world,",
        likes: 89,
        dislike: 2,
        slug: "article",
        daysAgo: 9,
      },
      {
        title: "Educational rights of minorities",
        description:
          "For children above the age of 17 years, the educational attainment of Muslims at matriculation is 17%, as against national average at 26%. ",
        likes: 62,
        dislike: 0,
        slug: "article",
        daysAgo: 2,
      },
      {
        title: "International day of happiness",
        description:
          "There's more behind the International Day of Happiness than you might think. Find out more by reading the article and answering the questions.",
        likes: 43,
        dislike: 1,
        slug: "article",
        daysAgo: 1,
      },
      {
        title: "International day of happiness",
        description:
          "There's more behind the International Day of Happiness than you might think. Find out more by reading the article and answering the questions.",
        likes: 89,
        dislike: 2,
        slug: "article",
        daysAgo: 1,
      },
    ],
    grades: [
      {
        categoryName: "Business",
        articlesRead: 45,
        averageScore: 87,
        slug: "grade",
      },
      {
        categoryName: "Finance",
        articlesRead: 25,
        averageScore: 92,
        slug: "grade",
      },
      {
        categoryName: "Food",
        articlesRead: 11,
        averageScore: 98,
        slug: "grade",
      },
      {
        categoryName: "Business",
        articlesRead: 45,
        averageScore: 87,
        slug: "grade",
      },
      {
        categoryName: "Business",
        articlesRead: 45,
        averageScore: 87,
        slug: "grade",
      },
    ],
  };

  const profileInfo = $("#profileInfo");
  const popularArticlesEl = $("#popularArticles");
  const grades = $("#grades");

  profileInfo.append(`<div class="card mb-3 col-12">
  <div class="row g-0">
    <div class="col-md-1 textAlign verticalAlign">
      <img src="logo.jpg" class="profilePic rounded" alt="..." />
    </div>
    <div class="col-md-11">
      <div class="card-body">
        <h3 class="card-title textAlignLeft">${profile.fullName}</h3>
        <p class="card-text">
            <small>@${profile.username}</small>
        </p>
        <p class="card-text">
          ${profile.description}
        </p>
        <a href="update.html"><button>Update</button></a>
      </div>
    </div>
  </div>
</div>`);

  profile.popularArticles.map((article) => {
    popularArticlesEl.append(`<a href="${article.slug}.html" class="linkNoDeco cardArticles">
    <div class="card card200px">
        <div class="card-body">
        <h5 class="card-title">${article.title}</h5>
        <h6 class="card-subtitle mb-2 text-muted">${article.daysAgo} days ago</h6>
        <p class="card-text textAlign">${article.description}</p>
        <div class="flex card-text">
                <div>Likes: ${article.likes}</div>
                <div>Likes: ${article.dislike}</div>
        </div>
        </div>
  </div>
  </a>`);
  });

  profile.grades.map((grade) => {
    grades.append(`<div class="card card200px">
      <div class="card-body">
      <h5 class="card-title">${grade.categoryName}</h5>
      <p class="card-text mt-2 textAlign">Articles read: ${grade.articlesRead}</p>
      <p class="card-text textAlign">Average score: ${grade.averageScore}</p>
      <div class="textAlign">
      <a href="${grade.slug}.html" class="card-text textAlign width100">See detailed results</a>
      </div>
      </div>
</div>`);
  });
});
