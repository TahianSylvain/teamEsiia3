
// console.log('hommeeeee');

/**
 * 
 * @param {String} element_name balise HTML
 * @param {String} class_name 
 */
 function _createElementWithClass(element_name, class_name) {
    let element = document.createElement(element_name)
    element.setAttribute('class', class_name)
    return element
}
