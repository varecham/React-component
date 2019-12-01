# React-component
Creates react component folder containing pre-generated index.js and &lt;component_name&gt;.js files so you'll have cleaner src folder and you may import components using:
```javascript
import [<Your-variable> from] '<component_name>'
```

1. Open package control with CTRL + SHIFT + P and go to "Install Package"
2. Type "React-component" and install.
3. Create in the root of your app a new *jsconfig.json* file (or *tsconfig.json* if you are using TypeScript) or add following code to the existing:
    ```javascript
    "include": [
        "src/**/*"
    ]
    ```
4. Right click on folder in sidebar menu where you want to generate a new React component.
5. Click on "New React component".
6. Type name of your new component and press Enter.

## Generated structure
`<component-name>` folder
- `<component-name>.js`
- `index.js` containing
    ```javascript
    export { default } from './<component-name>'
    ```
