const video_player = document.querySelector('#video_player'),
mainVideo = video_player.querySelector('#main-video'),
progressAreaTime = video_player.querySelector('.progressAreaTime'),
controls = video_player.querySelector('.controls'),
progressArea = video_player.querySelector('.progress-area'),
progress_Bar = video_player.querySelector('.progress-bar'),
controls_list = video_player.querySelector('.controls-list'),
fast_rewind = video_player.querySelector('.fast-rewind'),
play_pause = video_player.querySelector('.play_pause'),
fast_forward = video_player.querySelector('.fast-forward'),
volume = video_player.querySelector('.volume'),
volume_range = video_player.querySelector('.volume_range'),
current = video_player.querySelector('.current'),
totalDuration = video_player.querySelector('.duration'),
picture_in_picture = video_player.querySelector('.picture_in_picture'),
fullscreen = video_player.querySelector('.fullscreen');


const play = video_player.querySelector('.play')
const pause = video_player.querySelector('.pause')

console.log("video_player");

// //play video function
// function playVideo(){
//     // play_pause.innerHTML = "pause";
//     play_pause.title = "play";
//     video_player.classList.add('paused')
//     mainVideo.play();
// }

// //pause video function
// function pauseVideo(){
//     // play_pause.innerHTML = "play_arrow";
//     play_pause.title = "pause";
//     video_player.classList.remove('paused')
//     mainVideo.pause();
// }

// play_pause.addEventListener('click', ()=>{
//     const isVideoPaused = video_player.classList.contains('paused');
//     isVideoPaused ? pauseVideo() : playVideo();
// })

pause.style.display = 'none'

//play video function
function playVideo(){
    // play_pause.innerHTML = "pause";
    play_pause.title = "play";
    play.style.display = 'none'
    pause.style.display = 'block'
    video_player.classList.add('played')
    mainVideo.play();
}

//pause video function
function pauseVideo(){
    // play_pause.innerHTML = "play_arrow";
    play_pause.title = "pause";
    pause.style.display = 'none'
    play.style.display = 'block'
    video_player.classList.remove('played')
    mainVideo.pause();
}

play.addEventListener('click', ()=>{
    // const isVideoPaused = video_player.classList.contains('played');
    // isVideoPaused ? pauseVideo() : playVideo();
    playVideo()
})
pause.addEventListener('click', ()=>{
    // const isVideoPaused = video_player.classList.contains('played');
    // isVideoPaused ? pauseVideo() : playVideo();
    pauseVideo()
})


mainVideo.addEventListener('play', ()=>{
    playVideo();

})

mainVideo.addEventListener('pause', ()=>{
    pauseVideo();
})

 //fast rewind video function
fast_rewind.addEventListener('click', ()=>{
    mainVideo.currentTime -= 10;
})

//fast forward video function
fast_forward.addEventListener('click', ()=>{
    mainVideo.currentTime += 10;
})

// load video duration
mainVideo.addEventListener("loadeddata", (e)=>{
    // console.log(e.target.duration);
    let videoDuration = e.target.duration;
    let totalMin = Math.floor(videoDuration / 60);
    let totalSec = Math.floor(videoDuration % 60);
    // console.log(totalSec);

    // if seconds are less then 10 add 0 at the begining
    totalSec < 10 ? totalSec = "0"+totalSec : totalSec;
    totalDuration.innerHTML = `${totalMin} : ${totalSec}`;
    

})

// current video duration
mainVideo.addEventListener('timeupdate', (e)=>{
    let currentVideoTime = e.target.currentTime;
    let currentMin = Math.floor(currentVideoTime / 60);
    let currentSec = Math.floor(currentVideoTime % 60);
    // if seconds are less then 10 add 0 at the begining
    currentSec < 10 ? currentSec = "0"+currentSec : currentSec;
    current.innerHTML = `${currentMin} : ${currentSec}`;

    let videoDuration = e.target.duration
    // progressbar width change
    let progressWidth = (currentVideoTime / videoDuration) * 100;
    progress_Bar.style.width = `${progressWidth}%`; 
    
    

})

//  ===== HIDE AND SHOW THE CONTROLS PANEL =====
mainVideo.addEventListener('playing', e => {
    
    controls.addEventListener('mouseout', (e) => {
        // console.log("out");
        hide_controls = setTimeout(
            () => {
                controls.style.opacity = 0
                controls_list.style.visibility = 'hidden'
        }, 1000)
    })

    controls.addEventListener('mouseover', () => {
        // console.log("enter");
        clearTimeout(hide_controls)
        controls.style.opacity = 1
        controls_list.style.visibility = 'visible'
    })

})

// SYSTEME PRESENCE REHEFA TAPITRA ILAY VIDEO
mainVideo.addEventListener('ended', () => {
    
    let presence_check = document.querySelector('input#attendance_state')
    presence_check.checked = true

    let attendance_state = $('#attendance_form').serialize()
    console.log(attendance_state);

    $.ajax({
        url: '',
        data: attendance_state,
        type: 'post',
        success: (res) => {
            console.log(data);
        },
        error: (err) => {

        }
    })

})

// let's update playing video current time on according to the progress bar width

progressArea.addEventListener('click', (e)=>{
    let videoDuration = mainVideo.duration;
    let progressWidthval = progressArea.clientWidth;
    let ClickOffsetX = e.offsetX;
    mainVideo.currentTime = (ClickOffsetX / progressWidthval) * videoDuration;
})

// change volume

function changeVolume(){
    mainVideo.volume = volume_range.value / 100;
    if (volume_range == 0) {
        // volume.innerHTML = "volume_off";
    }else if(volume_range.value < 40){
        // volume.innerHTML = "volume_down";
    }else{
        // volume.innerHTML = "volume_up";
    }
}

function muteVolume(){
    if (volume_range.value == 0) {
        volume_range.value = 80;
        mainVideo.volume = 0.8;
        // volume.innerHTML = "volume_up";
    }else {
        volume_range.value = 0;
        mainVideo.volume = 0;
        // volume.innerHTML = "volume_off";
    }
}

volume_range.addEventListener('change',()=>{
    changeVolume();
})

volume.addEventListener('click',()=>{
    muteVolume();
})

// Update progress are time and display block on mouse move
progressArea.addEventListener('mousemove',(e)=>{
    let progressWidthval = progressArea.clientWidth;
    let x = e.offsetX;
    progressAreaTime.style.setProperty('--x',`${x}px`);
    progressAreaTime.style.display = "block";
    let videoDuration = mainVideo.duration;
    let progressTime = Math.floor((x/progressWidthval)*videoDuration);
    let currentMin = Math.floor(progressTime / 60);
    let currentSec = Math.floor(progressTime % 60);
    // if seconds are less then 10 then add 0 at the begining
    currentSec < 10 ? currentSec = "0"+currentSec : currentSec;
    progressAreaTime.innerHTML = `${currentMin} : ${currentSec}`;
    if(currentMin<0 || currentSec<0) {
        progressAreaTime.style.display = 'none'
    }
})

progressArea.addEventListener('mouseleave',()=>{
    progressAreaTime.style.display = "none";
})

// picture in picture

picture_in_picture.addEventListener('click',()=>{
    mainVideo.requestPictureInPicture();
})

// full screen function

fullscreen.addEventListener('click',()=>{
    if (!video_player.classList.contains('openFullScreen')){
        video_player.classList.add('openFullScreen');
        // fullscreen.innerHTML = "fullscreen_exit";
        video_player.requestFullscreen();
    }else {
        video_player.classList.remove('openFullScreen');
        // fullscreen.innerHTML = "fullscreen";
        document.exitFullscreen();
    }
})

// mouse move
video_player.addEventListener('mouveover',()=>{
    controls.classList.add('active');
})

video_player.addEventListener('mouveleave',()=>{
    if (video_player.classList.contains('paused')) {
        if (settingsBtn.classList.contains('active')) {
            controls.classList.add('active');
        } else {
            controls.classList.remove('active')
        }
    }else {
        controls.classList.add('active')
    }
})



// controls.addEventListener('mouseenter', e => {
// })

// document.addEventListener('mouseover', e => {
//     console.log(e.target);
// })