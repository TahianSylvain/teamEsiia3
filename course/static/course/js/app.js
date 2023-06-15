//console.log('hello');
const listVideo = document.querySelectorAll('.morevideos .desc-content');
const mainVideo = document.querySelector('.container video');
const titleVideo = document.querySelector('.desc .title .titlevideo');
const commentaire = document.querySelectorAll('.commentaire textarea');
const btn = document.querySelectorAll('.commentaire button');
console.log(btn);

listVideo.forEach(video => {
	video.onclick = () => {
		listVideo.forEach(vid => vid.classList.remove('active'));
		video.classList.add('active');

		if (video.classList.contains('active')) {
			let src = video.children[0].getAttribute('src');
			//console.log(src);
			mainVideo.src = src;
			let text = video.children[1].innerHTML;
			titleVideo.innerHTML = text; 
		}
	};
});
// btn.addEventListener('click', function(e){
// 	console.log(e.target);
// });