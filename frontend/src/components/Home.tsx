const Home = () => {
  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-4xl font-bold mb-6">Welcome to Digital Theatre</h1>
      <div className="prose lg:prose-xl">
        <p className="text-xl text-gray-600 mb-4">
          Experience theatre in a new way with AI-powered voice performances and interactive reading.
        </p>
        <div className="grid md:grid-cols-2 gap-8 mt-8">
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-2xl font-bold mb-4">Featured Plays</h2>
            <p className="text-gray-600">
              Discover our collection of classic and contemporary plays, brought to life through technology.
            </p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-2xl font-bold mb-4">How It Works</h2>
            <p className="text-gray-600">
              Select a play, customize the voices, and enjoy an immersive reading experience.
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Home