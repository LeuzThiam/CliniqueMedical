
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Register from './pages/Auth/register'


export default function App(){
  return(
    <Router>
      <Routes>
        <Route path="/register" element={<Register/>}/>
      </Routes>
    </Router>
  );
}