import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { ConfigProvider } from 'antd';

const rootEl = document.getElementById('root');
if (rootEl) {
  const root = ReactDOM.createRoot(rootEl);
  root.render(
    <React.StrictMode>
      <ConfigProvider
        theme={{
          components: {
            Table: {
              cellPaddingBlock: 22,
              headerBg: '#323D4E',
              colorBgContainer: '#273142',
              colorSplit: 'transparent',
              headerColor: '#fffffff2',
              stickyScrollBarBg: '#323D4E',
              stickyScrollBarBorderRadius: 100,
              borderColor: '#e0e0e033',
              lineWidth: 0.6,
              colorText: '#ffffffe6',
            },
          },
        }}
      >
        <App />
      </ConfigProvider>
    </React.StrictMode>
  );
}
