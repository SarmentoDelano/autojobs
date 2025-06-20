// src/components/FilterSidebar.jsx
function FilterSidebar() {
  return (
    <aside className="bg-[#13293D] text-white w-64 p-4 space-y-6">
      <div>
        <h2 className="text-lg font-semibold mb-2">Filtros</h2>
        <div className="space-y-2">
          <label className="flex items-center gap-2">
            <input type="checkbox" className="accent-[#1B98E0]" />
            Gupy
          </label>
          <label className="flex items-center gap-2">
            <input type="checkbox" className="accent-[#1B98E0]" />
            InfoJobs
          </label>
          <label className="flex items-center gap-2">
            <input type="checkbox" className="accent-[#1B98E0]" />
            Programathor
          </label>
          <label className="flex items-center gap-2">
            <input type="checkbox" className="accent-[#1B98E0]" />
            RemoteOK
          </label>
        </div>
      </div>

      <div>
        <h3 className="text-sm font-semibold mb-2">Filtrar por palavra-chave</h3>
        <input
          type="text"
          placeholder="Ex: React, Python"
          className="w-full px-2 py-1 rounded-md text-black"
        />
      </div>

      <button className="w-full bg-[#006494] hover:bg-[#247BA0] text-white font-medium py-2 rounded-md">
        Aplicar filtros
      </button>
    </aside>
  );
}

export default FilterSidebar;
