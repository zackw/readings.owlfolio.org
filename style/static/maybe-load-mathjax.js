(function (document) {
    "use strict";

    function maybeLoadMathML () {
        var findMath = document.getElementsByTagName("math");
        var cfg, script;
        if (findMath.length) {
            cfg = document.createElement("script");
            cfg.setAttribute("type", "text/x-mathjax-config");
            cfg.appendChild(document.createTextNode(
'MathJax.Hub.Config({extensions:["FontWarnings.js","MatchWebFonts.js"],"HTML-CSS":{preferredFont:"STIX",webFont:"STIX-Web",imageFont:null},FontWarnings:{webFont:null},MathMenu:{showLocale:false}})'));
            document.body.appendChild(cfg);

            script = document.createElement("script");
            script.async = true;
            script.src = "/s/MathJax.48b594af/MathJax.js?config=MML_HTMLorMML.js";
            document.body.appendChild(script);
        }
    }

    document.addEventListener('DOMContentLoaded', maybeLoadMathML);
})(document);
