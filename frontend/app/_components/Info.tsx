import React from 'react';
import '../_styles/styles.css';

const Info: React.FC<any> = () => {
  return (
    <div className="info flex flex-col p-2 gap-2">
      <div>
        <a href="https://github.com/jatolentino/" target="_blank">
          <img src="./github.svg"/>
        </a>
      </div>
      <div>
        <a href="https://www.figma.com/design/58ZQFWsitZKxSk0LYSwUj8/UI%2FUX-Solution-Jose-Tolentino?node-id=0-1&t=XIogI6Bpki8Wbkzm-1" target="_blank">
          <img src="./figma.svg"/>
        </a>
      </div>
      <div>
        <a href="https://hub.docker.com/r/joseaidocker/nextflask/tags" target="_blank">
          <img src="./docker.svg"/>
        </a>
      </div>


    </div>
  );
};

export default Info;
