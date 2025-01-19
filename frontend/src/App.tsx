import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Navbar from './components/navigation/Navbar'
import PlayList from './components/plays/PlayList'
import PlayReader from './components/plays/PlayReader'
import Home from './components/Home'

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <Navbar />
        <main className="container mx-auto px-4 py-8">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/plays" element={<PlayList />} />
            <Route path="/plays/:id" element={<PlayReader />} />
          </Routes>
        </main>
      </div>
    </Router>
  )
}

export default App