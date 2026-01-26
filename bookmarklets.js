// Use https://mrcoles.com/bookmarklet/ to turn this Javascript code into a button called Hide Comments
// which will hide the comment block that shows up after each question in the traditional rubric

let comments = document.getElementsByClassName('css-14i6tzz-view');
for (let i = 0; i < comments.length; i++)
{
    comments.item(i).style.display = 'None';
}
document.getElementsByClassName('css-96my1g-view').item(0).style.display = 'None';
