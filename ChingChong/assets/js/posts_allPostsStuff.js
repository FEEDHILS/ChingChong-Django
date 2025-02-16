const LikesDislikes = [];
function updateSprites() {
    const relations = document.querySelectorAll(".LikesAndDislikes"); 
    relations.forEach(relation => {
        buttons = relation.querySelectorAll("img");

        // console.log( buttons[0].dataset.pressed )
        // console.log( buttons[1].dataset.pressed )

        if (buttons[0].dataset.pressed == "True") {
            buttons[0].src = window.likeSprites.pressed;
            buttons[1].dataset.pressed = "False";
            buttons[1].src = window.dislikeSprites.normal;
        }
        else {
            buttons[0].src = window.likeSprites.normal;
        }

        if (buttons[1].dataset.pressed == "True") {
            buttons[1].src = window.dislikeSprites.pressed;
            buttons[0].dataset.pressed = "False";
            buttons[0].src = window.likeSprites.normal;
        }
        else {
            buttons[1].src = window.dislikeSprites.normal;
        }

    });
}

document.addEventListener("DOMContentLoaded", function() {
    updateSprites();

    // Пары Лайк/Дизлайк каждого поста
    document.querySelectorAll(".row.LikesAndDislikes").forEach(item => {
        objects = item.querySelectorAll(".row");
        LikesDislikes.push( [objects[0], objects[1]] );
    });

    // Слушаем отдельно каждую пару
    LikesDislikes.forEach(pair => {
        const like = pair[0].querySelector("img");
        const likeText = pair[0].querySelector(".amountL.p1");

        const dislike = pair[1].querySelector("img");
        const dislikeText = pair[1].querySelector(".amountD.p1");
        
        // Нажатие на Лайк
        like.addEventListener("click", function () {
            let likeAmount = parseInt(likeText.textContent);
            let dislikeAmount = parseInt(dislikeText.textContent);

            if (like.dataset.pressed == "True") {
                like.dataset.pressed = "False";
                likeAmount--;
            } 
            else {
                // На случай если была выбрана противоположная оценка до этого, меняем её и убираем дизлайк
                if (dislike.dataset.pressed == "True") {
                    dislike.dataset.pressed = "False";
                    dislikeAmount--;
                }

                like.dataset.pressed = "True";
                likeAmount++;
            }

            likeText.textContent = likeAmount;
            dislikeText.textContent = dislikeAmount;
            updateSprites();
        });

        // Нажатие на дизлайк
        dislike.addEventListener("click", function () {
            let likeAmount = parseInt(likeText.textContent);
            let dislikeAmount = parseInt(dislikeText.textContent); 

            if (dislike.dataset.pressed == "True") {
                dislike.dataset.pressed = "False";
                dislikeAmount--;
            } 
            else {
                // Аналогично
                if (like.dataset.pressed == "True") {
                    like.dataset.pressed = "False";
                    likeAmount--;
                }

                dislike.dataset.pressed = "True";
                dislikeAmount++;
            }

            likeText.textContent = likeAmount;
            dislikeText.textContent = dislikeAmount;
            updateSprites();
        });
    });
});
// document.querySelectorAll(".LikesAndDislikes").forEach(relation => {
//     relation.querySelectorAll(".btn.Icona").forEach(button => {
//         button.addEventListener("click", function () {
//             // console.log(button);
//             // console.log(relation);
//             img = button.children[0];
//             if (img.dataset.pressed == "True") {
//                 img.dataset.pressed = "False";
//             }
//             else {
//                 relation.querySelectorAll(".btn.Icona").forEach(button => {

//                 })
//                 img.dataset.pressed = "True";
//             }
//             console.log(button);

//             updateSprites();
//         });
//     });
// });