import { createGlobalStyle } from "styled-components";
import NunitoSansExtraBold from './assets/fonts/NunitoSans_7pt_Expanded-ExtraBold.ttf';
import NunitoSansBold from './assets/fonts/NunitoSans_7pt_Expanded-Bold.ttf';
import NunitoSansSemiBold from './assets/fonts/NunitoSans_7pt_Expanded-SemiBold.ttf';
import ActayWideBold from './assets/fonts/ActayWide-Bold.otf';
import ActayRegular from './assets/fonts/Actay-Regular.otf';
import Monocraft from './assets/fonts/Monocraft.otf';


export const GlobalStyles = createGlobalStyle`
  @font-face {
    font-family: 'Nunito Sans';
    font-style: normal;
    font-weight: 800;
    font-display: swap;
    src: url(${NunitoSansExtraBold}) format('truetype');
  }

  @font-face {
    font-family: 'Nunito Sans';
    font-style: normal;
    font-weight: 700;
    font-display: swap;
    src: url(${NunitoSansBold}) format('truetype');
  }

  @font-face {
    font-family: 'Nunito Sans';
    font-style: normal;
    font-weight: 600;
    font-display: swap;
    src: url(${NunitoSansSemiBold}) format('truetype');
  }

  @font-face {
    font-family: 'Actay Wide';
    font-style: normal;
    font-weight: 700;
    font-display: swap;
    src: url(${ActayWideBold}) format('opentype');
  }

  @font-face {
    font-family: 'Actay';
    font-style: normal;
    font-weight: 400;
    font-display: swap;
    src: url(${ActayRegular}) format('opentype');
  }

  @font-face {
    font-family: 'Monocraft';
    font-style: normal;
    font-weight: 500;
    font-display: swap;
    src: url(${Monocraft}) format('opentype');
  }

  body {
    margin: 0;
    background-color: #1b2431;
    font-family: Actay, Helvetica, Arial, sans-serif;
    color: #ffffff;

    & *::-webkit-scrollbar {
      height: 16px;
      width: 16px;
      background: transparent !important;
    }

    & *::-webkit-scrollbar-track {
      background-color: transparent !important;
    }

    & *::-webkit-scrollbar-thumb {
      background-color: #323D4E !important;
      border: 4px solid transparent;
      border-radius: 8px;
      background-clip: padding-box;
    }

    & *::-webkit-scrollbar-corner {
      background-color: transparent !important;
    }
  }

  #root {
    width: 100vw;
    height: 100vh;
  }

  * {
    box-sizing: border-box;
  }
`;
