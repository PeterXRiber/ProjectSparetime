
const container = document.querySelector("#container");

const content = document.createElement("div");
content.classList.add("content");
content.textContent = "This is the glorious text-content!";
container.appendChild(content);

// Step 1: create the variable and choose node
const btn = document.querySelector("#btn");
// Step 2: create some function
function alertFunction() {
    alert("YAY! YOU DID IT!");
}
// Step 3: add them both together in an EventListener. 
// The first argument will be the action that is performed from a user
btn.addEventListener("click",alertFunction);

btn.addEventListener("click", function (e) {
    e.target.style.background = "red"
});

const buttons = document.querySelectorAll("button");

buttons.forEach((button) => {
    
    button.addEventListener("click", () => {
        alert(button.id);
    });

});

const paragraph = document.createElement("p");

paragraph.textContent = "Hey I'm red!";
paragraph.style.cssText = "color: red;";
container.appendChild(paragraph);

const lesserHeadline = document.createElement("h3");

lesserHeadline.textContent = "I'm a blue h3!";
lesserHeadline.style.cssText = "color: blue;";
container.appendChild(lesserHeadline);

const secondContent = document.createElement("div");
secondContent.setAttribute ("style","border: solid; border-color: black; background: pink;");
container.appendChild(secondContent);

const pinkHeadline = document.createElement("h1");
const pinkParagraph = document.createElement("p");
secondContent.appendChild(pinkHeadline);
secondContent.appendChild(pinkParagraph);

pinkHeadline.textContent = "I'm in a div";
pinkParagraph.textContent = "Me TOO!";







