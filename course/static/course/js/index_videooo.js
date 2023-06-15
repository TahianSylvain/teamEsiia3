
document.addEventListener('DOMContentLoaded', () => {

    const
    aside_header_nav = document.querySelector('.aside_header_nav'),
    comment_content = document.querySelector('.comment_content'),
    related_content = document.querySelector('.related_content'),
    desc_content = document.querySelector('.desc_content'),
    aside_content = document.querySelector('.aside_content'),
    comment_textarea = document.querySelector('.comment_field textarea'),
    comment_list = document.querySelector('.comment_list')
    btns = Array.prototype.slice.call(aside_header_nav.children)

    comment_textarea.value = ''

    let scroll_container = document.querySelector('.comment_content > div:nth-child(1)')
    // scroll_container.addEventListener('scroll', e => {
    //     console.log(scroll_container.scrollTop)
    // })
    scroll_container.scrollTop = comment_list.offsetHeight 
    // console.log(`=>${scroll_container.scrollTop}`)

    // console.log('aaaa');

    // ASIDE NAVIGATION
    btns.forEach( btn => {
        btn.addEventListener('mouseover', () => {
            btn.classList.add('hover')
        })
        btn.addEventListener('mouseout', () => {
            btn.classList.remove('hover')
        })
        btn.addEventListener('click', function() {
            for(let sibling of btn.parentNode.children) {
                if (sibling !== btn) sibling.classList.remove('active')
            }
            btn.classList.add('active')

            for(let content of aside_content.children) {
                let content_act
                if(btn.classList.contains('comment_btn') && content.classList.contains('comment_content')) {
                    content_act = content
                    content_act.classList.add('active')
                }
                else if(btn.classList.contains('related_btn') && content.classList.contains('related_content')) {
                    content_act = content
                    content_act.classList.add('active')
                }
                else if(btn.classList.contains('desc_btn') && content.classList.contains('desc_content')) {
                    content_act = content
                    content_act.classList.add('active')
                }
                if(content !== content_act) content.classList.remove('active')
            }

        })
    })


    // COMMENTAIRE
    const send_comment = document.querySelector('#send_comment')

        send_comment.addEventListener('click', (e) => {
            // e.preventDefault
            var serializedData = $('#comment_form').serialize()
            console.log(serializedData);
            
            comment_textarea.value = ''

            $.ajax({
                url:$("comment_form").data('url'),
                data: serializedData,
                type: 'post',
                success: (res) => {
                    // console.log(res.comment);
                    $('.comment_list').append(
                        `<div class="comment latest">
                            <div class="comment_id_img">
                                <img src="${res.comment.pdp}" alt="" width="30px">
                            </div>
                            <div class="comment__">
                                <label> ${res.comment.one_name} </label>
                                <p>${res.comment.mess}</p>
                            </div>
                        </div>`
                    )
                    scroll_container.scrollTop = comment_list.offsetHeight
                },
                error: (err) => {
                    console.log(err);
                }
                
            })
            
            // console.log(`=====>${comment_list.offsetHeight}`)
            // console.log(`===>${scroll_container.scrollTop}`)

            // let latest = document.querySelector('.latest')
            // latest.scrollIntoView()
            // console.log(comment_list.scrollHeight);
            // comment_list.scrollTop = comment_list.scrollHeight
            // console.log(comment_list.scrollTop);

        })

})
