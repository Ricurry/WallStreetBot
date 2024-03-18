import fetch from 'node-fetch';

let Current = ''

fetch('https://www.reddit.com/r/fragranceclones/new.json?limit=10000&t=week')
    .then(function(res) 
    {
        return res.json();
    })
    .then(function(res) 
    {
        const posts = res.data.children;
        let CurrPost = ' ';
        for (let i = 0; i < posts.length; i++) 
        {
            CurrPost = posts[i].data;
            Current = CurrPost.title.split(',').join(' ');
            console.log(Current);
        }      
    })
    .catch(function(err) 
    {
        console.log(err);
    });