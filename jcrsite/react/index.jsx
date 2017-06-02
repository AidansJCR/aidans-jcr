/**
 * Created by ryan on 18/05/17.
 */
var React = require('react');
var ReactDOM = require('react-dom');

// first, we create a class that allows us to load
// the correct page, based on template

class AppMaker {
    static getApp() {
        return null;
    }
}








// class Hello extends React.Component {
//     render() {
//         return(
//             <h1>
//                 Hello, welcome to Aidan's JCR
//             </h1>
//         )
//     }
// }

ReactDOM.render(AppMaker.getApp(), document.getElementById('container'));