const asin_regex = /(?:[/dp/]|$)([A-Z0-9]{10})/

window.addEventListener("DOMContentLoaded", (event) => { 

    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        // since only one tab should be active and in the current window at once
        // the return variable should only have one entry
        var activeTab = tabs[0];
        const url = activeTab.url
        const matches = url.match(asin_regex)  
        let asin = (matches != null) ? matches[0].replace('/', '') : null;

        if (asin == null) {
            return;
        }

        fetchData(`http://127.0.0.1:5000/reviews/${asin}`)
            .then(data => {
                const container = document.querySelector(".container")
                if (data.length > 0) {
                    document.querySelector("#spinner").style.display = 'none'
                }
                sortedList = Array.from(data).sort(sortBySentiment)
                console.log(sortedList)
                
                sortedList.forEach(review => {
                    render(review, container)
                })
            })
    });    
})

async function fetchData(url) {
    const endpoint = url
    const response = await fetch(endpoint)
    const jsonData = await response.json()
    return jsonData
}

function sortBySentiment(a, b) {
    return Math.abs(b['sentiment'])- Math.abs(a['sentiment'])
}

function render(review, container) {
    const keyword = review['keyword']
    const sentiment = review['sentiment']
    const sentence = review['sentence']

    const textRow = document.createElement("div")
    textRow.textContent = keyword
    textRow.classList.add("box")
    textRow.setAttribute("title", sentence)

    const scoreNode = document.createElement("div")
    scoreNode.textContent = sentiment
    scoreNode.classList.add("box")

    if (parseFloat(sentiment) > 0) {
        textRow.classList.add("up-review")
        scoreNode.classList.add("up-score")
    } else {
        textRow.classList.add("down-review")
        scoreNode.classList.add("down-score")
    }

    container.appendChild(textRow)
    container.appendChild(scoreNode)
}