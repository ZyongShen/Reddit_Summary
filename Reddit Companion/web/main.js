var subreddit = 'UConn'

function subredditInput() {
    var ad = document.getElementById('advancedSearch')
    ad.innerHTML = ''
    var spot = document.getElementById('subreddit-input')
    spot.innerHTML = '<div class="input-group mb-3"> <div class="input-group-prepend"> <span class="input-group-text" id="subreddit-input">Subreddit</span> </div> <input type="text" id="subreddit-change" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"> <button type="button" class="btn btn-primary" onclick="displaySubreddit(); hideSubreddit()">Change</button> </div>'
    subreddit = document.getElementById('subreddit-input').value

}



function advancedInput() {
    var display = document.getElementById('displayReddit')
    display.innerHTML = ''
    var subR = document.getElementById('subreddit-input')
    subR.innerHTML = ''
    var spot = document.getElementById('advancedSearch')
    spot.innerHTML = '<div class="input-group mb-3"> <div class="input-group-prepend"> <span class="input-group-text" id="subreddit-input">Keywords</span> </div> <input id="inputs" type="text" id="advanceS" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"> <button type="button" class="btn btn-primary" onclick="findResults()">Search</button> </div>'
}


function hideInputs() {
    var subR = document.getElementById('subreddit-input')
    var ad = document.getElementById('advancedSearch')
    subR.innerHTML = ''
    ad.innerHTML = ''

}


function findResults() {
    var inputs = document.getElementById('inputs').value
    eel.advancedSearch(subreddit, inputs) (function(ret) {
        for (i=0; i < ret.length; i++) {
            display.innertHTML += 'works'
        }
    })
}