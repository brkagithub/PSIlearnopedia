$(document).ready(() => {
  const categories = ["Family", "Lifestyle", "Holiday", "Food"];

  const categoriesEl = $("#categories");

  const article = {
    title: "Title of this beautiful article",
    content: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nunc velit, rhoncus sit amet sapien a, lacinia dapibus enim. Mauris vitae dictum est. Sed quis hendrerit felis. Curabitur pretium neque nunc, quis vehicula tellus pellentesque in. Maecenas eget viverra eros, id tincidunt mi. Vivamus feugiat nibh et nulla sodales, id tincidunt orci fermentum. Donec tincidunt congue laoreet. Aenean fermentum odio ante, nec ornare mi molestie vel. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam congue, neque in pulvinar ornare, risus eros tempor nunc, sit amet malesuada diam risus non lorem. Aliquam semper sem in commodo egestas. In vehicula, tellus ut hendrerit vestibulum, orci lorem sagittis tellus, vitae posuere urna mauris quis risus. In elit urna, lobortis a molestie vitae, pellentesque vitae mauris. Praesent gravida et tellus nec lobortis. Pellentesque at orci facilisis, consequat leo vitae, pellentesque nibh.
      
      Vestibulum molestie ipsum quis leo sodales vestibulum.Suspendisse cursus justo a egestas congue.Vestibulum hendrerit ligula quis nisi aliquam, at venenatis odio condimentum.Nunc at blandit lacus.Phasellus maximus sit amet purus nec malesuada.Integer facilisis, sapien at finibus finibus, libero neque ultrices risus, eget lacinia sem mi a nisl.Praesent diam tortor, eleifend in mi sed, porta sollicitudin felis.Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.Sed mattis elit dictum varius consequat.
      
      Curabitur id auctor magna, ut efficitur eros. Integer volutpat interdum eros, nec vulputate orci pulvinar at. Quisque vulputate nibh ac tempus hendrerit. Aenean pellentesque volutpat nunc, ac ullamcorper lacus tempus ut. Mauris at turpis gravida, viverra nunc in, ullamcorper ipsum. Vestibulum dignissim, augue a hendrerit vehicula, elit risus tincidunt ex, eu ornare risus tortor lobortis odio. Aenean condimentum arcu eget molestie dapibus. Curabitur ante leo, tempus eget sapien nec, tempor consectetur dolor.
      
      Praesent vulputate turpis a condimentum dapibus. Integer non turpis at nunc luctus fringilla. Etiam ornare ante sed urna semper ultricies. Etiam eget dictum felis, eu rutrum sapien. Suspendisse porttitor risus blandit dignissim volutpat. Fusce enim massa, pretium ac nibh at, malesuada vulputate velit. Morbi et nisl imperdiet nibh accumsan commodo. Praesent dapibus libero suscipit odio accumsan volutpat. Suspendisse rutrum a ipsum vitae porttitor. Duis ac felis tempus diam molestie scelerisque. Sed molestie suscipit ligula, sit amet fringilla ex molestie vitae. Integer gravida, odio quis tempus molestie, augue elit blandit turpis, at tempus purus mi a elit. Etiam non neque ut ipsum placerat accumsan. Cras pretium pretium dignissim.
      
      Quisque commodo nibh purus, ut pharetra eros sollicitudin id. Aenean sit amet leo et odio blandit commodo. Etiam laoreet lorem id turpis sodales, quis tempus magna aliquam. Nulla scelerisque, lorem sollicitudin gravida mollis, est sem vulputate orci, sit amet convallis mauris arcu ac diam. Aliquam eget dui suscipit, cursus nisi in, cursus massa. Fusce ullamcorper auctor eros, in ornare urna. Suspendisse suscipit tortor dui, sit amet imperdiet tortor viverra at. Proin facilisis malesuada felis sit amet pretium. Donec quis cursus nunc. Suspendisse eu leo eleifend, lobortis diam vitae, efficitur sapien. Etiam accumsan porta massa, sed vulputate felis feugiat et. Etiam non vehicula diam.`,
    author: {
      name: "Jessica Wildfire",
      profileSlug: "profile",
      totalLikes: 5555,
      articles: [
        {
          title: "Impact of global warming to the North Pole",
          slug: "article",
        },
        { title: "Impact of Tiktok to mental health", slug: "article" },
        {
          title: "Impact of advancing AI to the food industry",
          slug: "article",
        },
      ],
    },
  };

  const title = $("#title");

  const authorEl = $("#author");

  const contentEl = $("#content");

  categories.map((categoryName) => {
    categoriesEl.append(
      `<a href="${categoryName}.html" class="textNoDeco"><button class="rounded-circle categoryChip">${categoryName}</button></a>`
    );
  });

  /*authorEl.append(`<h3>profile pic</h3>
    <a href="${article.author.profileSlug}.html"> <h3 class="underlinedAuthor">${article.author.name}</h3></a>
    <p>Total likes: ${article.author.totalLikes}</p>
    <h6>From same author</h6>`);*/

  article.author.articles.map((article) => {
    authorEl.append(
      `<a href="${article.slug}.html"><h5>${article.title}</h5></a>`
    );
  });

  //title.html(article.title);

  //contentEl.append(`<div class="mt-20">${article.content}</div>`);
});
