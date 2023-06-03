var foldable = document.querySelectorAll(".one-post .folding-button");
for (var i = 0; i < foldable.length; i++) {
    foldable[i].addEventListener("click", function (event) {
        if (event.target.parentElement.classList.contains("folded")) {
            event.target.parentElement.classList.remove("folded")
        } else {
            event.target.parentElement.classList.add("folded")
        }
    })
}
