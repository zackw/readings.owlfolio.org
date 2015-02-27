(function (document) {
    "use strict";

    function maybeLoadMathML () {
        var findMath = document.getElementsByTagName("math");
        var script;
        if (findMath.length) {
            script = document.createElement("script");
            script.async = true;
            script.src = "/s/MathJax/MathJax.js?config=MML_HTMLorMML.js";
            document.body.appendChild(script);
        }
    }

    document.addEventListener('DOMContentLoaded', maybeLoadMathML);
})(document);
