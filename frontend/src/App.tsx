import './App.css';
import { LoginPage } from './pages/LoginPage';
import { MainPage } from './pages/MainPage';
 import { RegisterPage } from './pages/RegisterPage';
import { ChangePassPage } from './pages/ChangePassPage';
// import { LoginPage } from './pages/LoginPage';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/login' element={<LoginPage/>}/>
        <Route path='/singin' element={<RegisterPage/>}/>
        <Route path='/changepass' element={<ChangePassPage/>}/>
        <Route path='/main' element={<MainPage/>}/>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
